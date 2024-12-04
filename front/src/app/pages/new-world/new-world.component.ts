import { AsyncPipe } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { RouterLink } from '@angular/router';
import { map } from 'rxjs/operators';
import { Company } from '../../features/new-world/models/companies.interface';
import { CompaniesService } from '../../features/new-world/services/companies.service';
import { CompanyCardComponent } from '../../features/new-world/components/company-card/company-card.component';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-new-world',
  standalone: true,
  imports: [
    RouterLink,
    AsyncPipe,
    CompanyCardComponent
  ],
  templateUrl: './new-world.component.html',
  styleUrl: './new-world.component.scss'
})
export class NewWorldComponent implements OnInit {

  recentCompanies$!: Observable<Company[]>;

  constructor(private companiesService: CompaniesService) {}


  ngOnInit(): void {
    this.recentCompanies$ = this.companiesService.getCompaniesNewWorld().pipe(
      map(companies => companies.slice(0, 3))
    );
  }



}
