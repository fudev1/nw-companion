import { AsyncPipe, DatePipe } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { CharactersService } from '../../../services/characters.service';
import { Character } from '../../../models/character.interface';
import { map, Observable, switchMap } from 'rxjs';

@Component({
  selector: 'app-character-detail',
  standalone: true,
  imports: [
    AsyncPipe,
    DatePipe,
  ],
  templateUrl: './character-detail.component.html',
  styleUrl: './character-detail.component.scss'
})
export class CharacterDetailComponent implements OnInit {

  character$!: Observable<Character | undefined>;
  
  ngOnInit(): void {

    
    this.character$ = this.route.paramMap.pipe(
      map(params => params.get('id')),
      switchMap(id => this.charactersService.getUserCharacters().pipe(
        map(characters => characters.find(char => char.id === id))

      ))
    );
  }

  constructor(
    private route: ActivatedRoute,
    private charactersService: CharactersService
  ) {}

  getRoleClass(role: string): string {
    const baseClasses = 'px-2 py-1 text-xs font-medium rounded-full';
    switch (role) {
      case 'Tank':
        return `${baseClasses} bg-red-900 text-red-200`;
      case 'Healer':
        return `${baseClasses} bg-green-900 text-green-200`;
      case 'DPS':
        return `${baseClasses} bg-blue-900 text-blue-200`;
      default:
        return baseClasses;
    }
  }

}
