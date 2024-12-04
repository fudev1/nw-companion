import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-hero-main',
  standalone: true,
  imports: [
    RouterLink
  ],
  templateUrl: './hero-main.component.html',
  styleUrl: './hero-main.component.scss'
})
export class HeroMainComponent {

}
