import { Component } from '@angular/core';
import { CharactersService } from '../../../services/characters.service';
import { Observable } from 'rxjs';
import { Character } from '../../../models/character.interface';
import { OnInit } from '@angular/core';
import { AsyncPipe } from '@angular/common';
import { RouterLink } from '@angular/router';
import { WEAPONS, ROLES, SERVERS } from '../../../models/character.interface';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-character-list',
  standalone: true,
  imports: [
    AsyncPipe,
    RouterLink,
    FormsModule,
  ],
  templateUrl: './character-list.component.html',
  styleUrl: './character-list.component.scss'
})
export class CharacterListComponent implements OnInit {

  characters$!: Observable<Character[]>;
  showNewCharacterForm = false;
  weapons = WEAPONS;
  roles = ROLES;
  servers = SERVERS;

  newCharacter: Partial<Character> = {
    name: '',
    server: '',
    role: undefined,
    gearScore: 500,
    primaryWeapon: '',
    secondaryWeapon: ''
  };



  ngOnInit(): void {
    this.characters$ = this.charactersService.getUserCharacters();
  }

  constructor(private charactersService: CharactersService) {}

  get isFormValid(): boolean {
    return !!(
      this.newCharacter.name &&
      this.newCharacter.server &&
      this.newCharacter.role &&
      this.newCharacter.gearScore &&
      this.newCharacter.primaryWeapon &&
      this.newCharacter.secondaryWeapon
    );
  }


  createCharacter(): void {
    if (this.isFormValid) {
      this.charactersService.createCharacter({
        name: this.newCharacter.name!,
        server: this.newCharacter.server!,
        role: this.newCharacter.role as 'Tank' | 'Healer' | 'Support' | 'Bruiser' | 'Melee Dex' | 'Ranged Dex',
        gearScore: this.newCharacter.gearScore!,
        primaryWeapon: this.newCharacter.primaryWeapon!,
        secondaryWeapon: this.newCharacter.secondaryWeapon!
      });

      this.showNewCharacterForm = false;
      this.newCharacter = {
        name: '',
        server: '',
        role: undefined,
        gearScore: 500,
        primaryWeapon: '',
        secondaryWeapon: ''
      };
    }
  }

  getRoleClass(role: string): string {
    const baseClasses = 'px-2 py-1 text-xs font-medium rounded-full';

    switch (role) {
      case 'Tank':
        return `${baseClasses} bg-red-900 text-green-800`;
      case 'Healer':
        return `${baseClasses} bg-green-900 text-green-200`;
      case 'DPS':
        return `${baseClasses} bg-blue-900 text-blue-200`;
      default:
        return baseClasses;
    }
  }


}