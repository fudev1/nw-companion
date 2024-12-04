import { AsyncPipe } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormsModule, NgModel } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { CharactersService } from '../../../../features/new-world/services/characters.service';
import { Character, ROLES, WEAPONS } from '../../../new-world/models/character.interface';
import { Region, REGIONS, SERVERS } from '../../../new-world/models/guild.interface';
import { GuildsService } from '../../../new-world/services/guilds.service';
import { AuthService } from '../../../../core/services/auth.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-user-nw-guild',
  standalone: true,
  imports: [
    RouterLink,
    AsyncPipe,
    FormsModule,
  ],
  templateUrl: './user-nw-guild.component.html',
  styleUrl: './user-nw-guild.component.scss'
})
export class UserNwGuildComponent implements OnInit {

  currentStep = 1;
  characters$!: Observable<Character[]>; // Retard l'initialisation
  weapons = WEAPONS;
  roles = ROLES;
  regions = REGIONS;
  availableServers: string[] = [];
  selectedCharacterId: string | null = null;
  createdGuildId: string | null = null;

  newCharacter: Partial<Character> = {
    name: '',
    role: undefined,
    primaryWeapon: '',
    secondaryWeapon: ''
  };

  newGuild = {
    name: '',
    region: '',
    server: '',
    dkpEnabled: false,
    ownerCharacterId: ''
  };

  constructor(
    private charactersService: CharactersService,
    private guildsService: GuildsService,
    public auth: AuthService
  ) {}

  ngOnInit(): void {
    this.characters$ = this.charactersService.getUserCharacters();
  }

  createCharacter(): void {
    if (
      this.newCharacter.name &&
      this.newCharacter.role &&
      this.newCharacter.primaryWeapon &&
      this.newCharacter.secondaryWeapon
    ) {
      this.charactersService.createCharacter({
        name: this.newCharacter.name,
        role: this.newCharacter.role as 'Tank' | 'Healer' | 'Support' | 'Bruiser' | 'Melee Dex' | 'Ranged Dex',
        primaryWeapon: this.newCharacter.primaryWeapon,
        secondaryWeapon: this.newCharacter.secondaryWeapon
      });

      // Reset form
      this.newCharacter = {
        name: '',
        role: undefined,
        primaryWeapon: '',
        secondaryWeapon: ''
      };
    }
  }

  selectCharacter(character: Character): void {
    this.selectedCharacterId = character.id;
    this.newGuild.ownerCharacterId = character.id;
  }

  onRegionChange(region: string): void {
    this.newGuild.server = '';
    if (this.isValidRegion(region)) {
      this.availableServers = SERVERS[region];
    } else {
      this.availableServers = [];
    }
  }

  private isValidRegion(region: string): region is Region {
    return REGIONS.includes(region as Region);
  }

  get isGuildFormValid(): boolean {
    return !!(
      this.newGuild.name &&
      this.newGuild.region &&
      this.newGuild.server &&
      this.newGuild.ownerCharacterId
    );
  }

  nextStep(): void {
    if (this.currentStep < 3) {
      this.currentStep++;
    }
  }

  previousStep(): void {
    if (this.currentStep > 1) {
      this.currentStep--;
    }
  }

  createGuild(): void {
    if (this.isGuildFormValid) {
      this.guildsService.createGuild({
        name: this.newGuild.name,
        region: this.newGuild.region,
        server: this.newGuild.server,
        ownerCharacterId: this.newGuild.ownerCharacterId,
      });
      this.currentStep = 3;
    }
  }
}
