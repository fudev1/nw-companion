import { Routes } from '@angular/router';
import { MainLayoutComponent } from './core/layout/main-layout.component';
import { MainComponent } from './main/main.component';
import { NewWorldComponent } from './games/new-world/new-world.component';
import { PricingComponent } from './main/pricing/pricing.component';

export const routes: Routes = [
    {
        path: '',
        component: MainLayoutComponent,
        children: [
            { path: '', component: MainComponent },
            { path: 'new-world', component: NewWorldComponent},
            { path: 'pricing', component: PricingComponent},
        ]
    }
    // {
    //     path: 'home',
    //     loadComponent: () => new Promise(resolve => {
    //         setTimeout(() => {
    //             import('./landing/layout/main-layout.component').then(module => resolve(module.MainLayoutComponent));
    //         }, 20000); // 2-second delay to simulate loading
    //     }),
    // }
    // { 
    //     path: '',
    //     redirectTo: 'home',
    //     pathMatch: 'full', // redirige vers le component `home` par defaut
    // },
    // {
    //     path: 'home',
    //     component: HomeComponent,
    // },
    // {
    //     path: 'new-world',
    //     component: NwHomeComponent,
        
    // },
];
