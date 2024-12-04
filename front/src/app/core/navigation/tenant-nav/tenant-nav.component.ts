import { Component, Input } from '@angular/core';
import { Company } from '../../../features/new-world/models/companies.interface';
import { RouterLink, RouterLinkActive } from '@angular/router';
import { NgClass } from '@angular/common';
import { UserMenuComponent } from '../../components/user-menu/user-menu.component';

@Component({
  selector: 'app-tenant-nav',
  standalone: true,
  imports: [
    RouterLink,
    RouterLinkActive,
    NgClass,
    UserMenuComponent
  ],
  templateUrl: './tenant-nav.component.html',
  styleUrl: './tenant-nav.component.scss'
})
export class TenantNavComponent {

  @Input() company?: Company;

  navItems = [
    { path: 'members', label: 'Members' },
    { path: 'wars', label: 'Wars' },
    { path: 'events', label: 'Events' },
    { path: 'roster', label: 'Roster' },
  ];

}
