import { Component } from '@angular/core';
import { RouterOutlet, Router } from '@angular/router';
import { CommonModule } from '@angular/common';

import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { NewWorldHeaderComponent } from '../../games/new-world/header/header.component';
import { LoginButtonComponent } from "./login-button/login-button.component";

@Component({
  selector: 'app-main-layout',
  standalone: true,
  imports: [RouterOutlet, HeaderComponent, FooterComponent, NewWorldHeaderComponent, CommonModule ],
  templateUrl: './main-layout.component.html',
  styleUrl: './main-layout.component.scss'
})
export class MainLayoutComponent {
  isNewWorldContext: boolean = false; 

  constructor(private router: Router) {
    this.router.events.subscribe(() => {
      // vérifier si l'url commence par /new-world
      this.isNewWorldContext = this.router.url.startsWith('/new-world');
    });
  } 
}
