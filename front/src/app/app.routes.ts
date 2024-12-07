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
import { TenantLayoutComponent } from './core/layouts/tenant-layout/tenant-layout.component';
import { TenantNewWorldComponent } from './pages/tenant/tenant-new-world/tenant-new-world.component';
import { TenantNwWarsComponent } from './features/new-world/tenant/pages/tenant-nw-wars/tenant-nw-wars.component';
import { TenantNwMembersComponent } from './features/new-world/tenant/pages/tenant-nw-members/tenant-nw-members.component';
import { TenantNwRosterComponent } from './features/new-world/tenant/pages/tenant-nw-roster/tenant-nw-roster.component';
import { TenantNwEventsComponent } from './features/new-world/tenant/pages/tenant-nw-events/tenant-nw-events.component';
import { TenantNwApplyComponent } from './features/new-world/tenant/pages/tenant-nw-apply/tenant-nw-apply.component';
import { CharacterListComponent } from './features/new-world/components/character/character-list/character-list.component';
import { CharacterDetailComponent } from './features/new-world/components/character/character-detail/character-detail.component';



export const routes: Routes = [
    {
        path: '',
        component: MainLayoutComponent,
        children: [
            { path: '', component: HomeComponent },
            { path: 'about', component: AboutComponent},
            { path: 'contact', component: ContactComponent},
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
            { path: 'forum', component: ForumComponent},
            { 
                path: 'characters', 
                // component: CharactersComponent, 
                component: CharacterListComponent,
                canActivate: [authGuard],
                children: [
                    { path: '', component: CharacterListComponent },
                    { path: ':id', component: CharacterDetailComponent }
                ] 
            },
            // { path: 'guild', component: UserNwGuildComponent }
        ]
    },

    {
        path: 'new-world/company/:id',
        component: TenantLayoutComponent,
        children: [
            { path: '', component: TenantNewWorldComponent },
            { path: 'members', component: TenantNwMembersComponent},
            { path: 'wars', component: TenantNwWarsComponent}, 
            { path: 'roster', component: TenantNwRosterComponent},
            { path: 'events', component: TenantNwEventsComponent},
            { path: 'apply', component: TenantNwApplyComponent},
            // { path: 'characters', component: UserNwCharactersComponent },
            // { path: 'guild', component: UserNwGuildComponent }
        ]
    }
];
