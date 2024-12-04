import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive } from '@angular/router';
import { UserMenuComponent } from '../../components/user-menu/user-menu.component';
import { AuthService } from '../../services/auth.service';
import { AsyncPipe } from '@angular/common';

@Component({
  selector: 'app-new-world-nav',
  standalone: true,
  imports: [
    RouterLink,
    RouterLinkActive,
    UserMenuComponent,
    AsyncPipe,
  ],
  templateUrl: './new-world-nav.component.html',
  styleUrl: './new-world-nav.component.scss'
})
export class NewWorldNavComponent {
  
  newWorldNavItems = [ 
    { path: '/new-world/companies', label: 'Companies' },
    { path: '/new-world/wars', label: 'Wars' },
    { path: '/new-world/servers', label: 'Servers' },
    { path: '/new-world/news', label: 'News' },
    { path: '/new-world/forum', label: 'Forum' }
  ];

  constructor(public auth: AuthService) { }

}
