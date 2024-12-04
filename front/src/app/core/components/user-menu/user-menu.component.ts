import { Component } from '@angular/core';
import { AsyncPipe } from '@angular/common';

import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-user-menu',
  standalone: true,
  imports: [
    AsyncPipe,
  ],
  templateUrl: './user-menu.component.html',
  styleUrl: './user-menu.component.scss'
})
export class UserMenuComponent {

  isMenuOpen = false; 

  constructor(public auth: AuthService) { }

  toggleMenu(): void {
    this.isMenuOpen = !this.isMenuOpen;
  }

  login(): void {
    this.auth.login();
  }

  logout(): void {
    this.auth.logout();
    this.isMenuOpen = false;
  }


}
