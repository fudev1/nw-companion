import { Routes } from '@angular/router';
import { authGuard } from './core/guards/auth.guard';

import { MainLayoutComponent } from './core/layouts/main-layout/main-layout.component';
import { NewWorldLayoutComponent } from './core/layouts/new-world-layout/new-world-layout.component';

import { HomeComponent } from './pages/home/home.component';
import { AboutComponent } from './pages/about/about.component';
import { NewWorldComponent } from './pages/new-world/new-world.component';
import { CompaniesComponent } from './features/new-world/pages/companies/companies.component';
import { WarsComponent } from './features/new-world/pages/wars/wars.component';
import { ForumComponent } from './features/new-world/pages/forum/forum.component';
import { ContactComponent } from './pages/contact/contact.component';
import { ServersComponent } from './features/new-world/pages/servers/servers.component';
import { NewsComponent } from './features/new-world/pages/news/news.component';



export const routes: Routes = [
    {
        path: '',
        component: MainLayoutComponent,
        children: [
            { path: '', component: HomeComponent },
            { path: 'about', component: AboutComponent},
            { path: 'contact', component: ContactComponent},
            { path: 'characters', component: ContactComponent, canActivate: [authGuard] },
        ]
    },

    {
        path: 'new-world',
        component: NewWorldLayoutComponent,
        children: [
            { path: '', component: NewWorldComponent },
            { path: 'companies', component: CompaniesComponent },
            { path: 'wars', component: WarsComponent },
            { path: 'servers', component: ServersComponent },
            { path: 'news', component: NewsComponent },
            { path: 'forum', component: ForumComponent}
        ]
    }
];
