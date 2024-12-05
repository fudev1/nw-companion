import { Injectable } from '@angular/core';
import { Character } from '../models/character.interface';
import { BehaviorSubject, Observable, map, switchMap } from 'rxjs';
import { CHARACTERS } from '../data/characters.mock';
import { AuthService } from '../../../core/services/auth.service';


@Injectable({
  providedIn: 'root'
})
export class CharactersService {
  
  private characters = new BehaviorSubject<Character[]>(CHARACTERS);

  constructor(private auth: AuthService) {}

  getUserCharacters(): Observable<Character[]> {
    return this.auth.currentUser$.pipe(
      switchMap(user => 
        this.characters.pipe(
          map(characters => 
            characters.filter(char => char.userId === user?.id)
          )
        )
      )
    );
  }

  createCharacter(character: Omit<Character, 'id' | 'userId' | 'createdAt' | 'updatedAt'>): void {
    const user = this.auth.currentUser;
    if (!user) return;


    const newCharacter: Character = {
      ...character,
      id: crypto.randomUUID(),
      userId: user.id,
      createdAt: new Date(),
      updatedAt: new Date(),
    };

    this.characters.next([...this.characters.value, newCharacter]);
  }

  deleteCharacter(characterId: string): void {
    const updatedCharacters = this.characters.value.filter(
      char => char.id !== characterId
    );
    this.characters.next(updatedCharacters);
  }
}
