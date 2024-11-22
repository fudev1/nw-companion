import { Routes } from '@angular/router';
import { HomeComponent } from './public/home/home.component';
import { NwHomeComponent } from './new-world/home/home.component';

export const routes: Routes = [
    { 
        path: '',
        redirectTo: 'home',
        pathMatch: 'full', // redirige vers le component `home` par defaut
    },
    {
        path: 'home',
        component: HomeComponent,
    },
    {
        path: 'new-world',
        component: NwHomeComponent,
        
    },
];
