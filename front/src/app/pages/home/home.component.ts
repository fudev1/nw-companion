import { Component } from '@angular/core';
import { GameCardComponent } from './components/game-card/game-card.component';
import { HeroMainComponent } from './components/hero-main/hero-main.component';
import { SectionDashboardComponent } from './components/section-dashboard/section-dashboard.component';
import { Game } from '../../core/models/game.interface';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [
    GameCardComponent,
    HeroMainComponent,
    SectionDashboardComponent
  ],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent {

  games: Game[] = [
    {
      title: 'New World',
      description: 'A massively multiplayer online role-playing game (MMORPG) developed by Amazon.',
      imagePath: 'assets/images/games/new-world.png',
      path: '/new-world'
    },

    {
      title: 'Thrones & Liberty',
      description: "Organize your guild in NCSoft's upcoming MMORPG. Plan raids and manage your roster.",
      imagePath: 'assets/images/games/new-world.png',
      path: '/new-world'
    },
  ]

}
