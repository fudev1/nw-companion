import { AsyncPipe } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CharactersService } from '../../services/characters.service';
import { Character, WEAPONS, ROLES } from '../../models/character.interface';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-characters',
  standalone: true,
  imports: [
    AsyncPipe, 
    FormsModule,
  ],
  templateUrl: './characters.component.html',
  styleUrl: './characters.component.scss'
})
export class CharactersComponent implements OnInit {

  characters$!: Observable<Character[]>;
  showNewCharacterForm = false;
  weapons = WEAPONS;
  roles = ROLES;

  newCharacter: Partial<Character> = {
    name: '',
    role: 'undefined',
    primaryWeapon: '',
    secondaryWeapon: '',
  };

  ngOnInit(): void {
    this.characters$ = this.charactersService.getUserCharacters();
  }

  constructor(private charactersService: CharactersService) { }

  createCharacter(): void {
    if (
      this.newCharacter.name &&
      this.newCharacter.role &&
      this.newCharacter.primaryWeapon &&
      this.newCharacter.secondaryWeapon
    ) {
      this.charactersService.createCharacter({
        name: this.newCharacter.name,
        role: this.newCharacter.role,
        primaryWeapon: this.newCharacter.primaryWeapon,
        secondaryWeapon: this.newCharacter.secondaryWeapon,
      });

      this.showNewCharacterForm = false;
      this.newCharacter = {
        name: '',
        role: 'undefined',
        primaryWeapon: '',
        secondaryWeapon: '',
      };
    }
  }

}
