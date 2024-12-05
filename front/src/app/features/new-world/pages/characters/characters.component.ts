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
  showDeleteConfirm = false;
  characterToDelete: Character | null = null;
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

  get isFormValid(): boolean {
    return !!(
      this.newCharacter.name &&
      this.newCharacter.role &&
      this.newCharacter.primaryWeapon &&
      this.newCharacter.secondaryWeapon
    );
  }

  createCharacter(): void {
    if (this.isFormValid) {
      this.charactersService.createCharacter({
        name: this.newCharacter.name!,
        role: this.newCharacter.role!,
        primaryWeapon: this.newCharacter.primaryWeapon!,
        secondaryWeapon: this.newCharacter.secondaryWeapon!,
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

  confirmDelete(character: Character): void {
    this.characterToDelete = character;
    this.showDeleteConfirm = true;
  }

  cancelDelete(): void {
    this.characterToDelete = null;
    this.showDeleteConfirm = false;
  }

  deleteCharacter(): void {
    if (this.characterToDelete) {
      this.charactersService.deleteCharacter(this.characterToDelete.id);
      this.cancelDelete();
    }
  }
}
