import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive } from '@angular/router';
import { UserMenuComponent } from "../../components/user-menu/user-menu.component";

@Component({
  selector: 'app-main-nav',
  standalone: true,
  imports: [
    RouterLink,
    RouterLinkActive,
    UserMenuComponent
],
  templateUrl: './main-nav.component.html',
  styleUrl: './main-nav.component.scss'
})
export class MainNavComponent {

  mainNavItems = [
    { path: '/new-world', label: 'New World' },
    { path: '/thrones-liberty', label: 'Thrones Liberty' },
  ]

  secondaryNavItems = [
    { path: '/about', label: 'About' },
    { path: '/contact', label: 'Contact' }
  ]
}
