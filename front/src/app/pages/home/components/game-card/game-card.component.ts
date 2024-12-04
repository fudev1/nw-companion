import { Component, Input } from '@angular/core';
import { Game } from '../../../../core/models/game.interface';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-game-card',
  standalone: true,
  imports: [
    RouterLink
  ],
  templateUrl: './game-card.component.html',
  styleUrl: './game-card.component.scss'
})
export class GameCardComponent {

  @Input({ required: true }) game!: Game;
  
}
