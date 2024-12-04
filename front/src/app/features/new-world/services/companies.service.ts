import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { Company } from '../models/companies.interface';
import { COMPANIES } from '../data/companies.mock';

@Injectable({
  providedIn: 'root'
})
export class CompaniesService {

  getCompaniesNewWorld(): Observable<Company[]> {
    return of(COMPANIES);
  }

  getCompaniesNewWorldById(id: string): Observable<Company | undefined> {
    return of(COMPANIES.find(company => company.id === id));
  }

  constructor() { }
}
