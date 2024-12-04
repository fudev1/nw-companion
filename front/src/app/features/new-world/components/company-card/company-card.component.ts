import { Component, Input } from '@angular/core';
import { RouterLink } from '@angular/router';
import { Company } from '../../models/companies.interface';
import { NgClass } from '@angular/common';

@Component({
  selector: 'app-company-card',
  standalone: true,
  imports: [
    RouterLink,
    NgClass
  ],
  templateUrl: './company-card.component.html',
  styleUrl: './company-card.component.scss'
})
export class CompanyCardComponent {

  @Input({ required: true }) company!: Company;
  
}
