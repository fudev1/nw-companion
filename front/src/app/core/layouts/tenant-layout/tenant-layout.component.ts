import { Component, OnInit } from '@angular/core';
import { RouterOutlet, ActivatedRoute } from '@angular/router';
import { TenantNavComponent } from "../../navigation/tenant-nav/tenant-nav.component";
import { NgClass } from '@angular/common';
import { CompaniesService } from '../../../features/new-world/services/companies.service';
import { Company } from '../../../features/new-world/models/companies.interface';

@Component({
  selector: 'app-tenant-layout',
  standalone: true,
  imports: [
    RouterOutlet,
    TenantNavComponent,
    NgClass
],
  templateUrl: './tenant-layout.component.html',
  styleUrl: './tenant-layout.component.scss'
})
export class TenantLayoutComponent {

  company?: Company;

  constructor(
    private route: ActivatedRoute,
    private companiesService: CompaniesService
  ) {}

  ngOnInit() {
    const companyId = this.route.snapshot.paramMap.get('id');
    if (companyId) {
      this.companiesService.getCompaniesNewWorldById(companyId).subscribe(
        company => this.company = company
      );
    }
  }
}
