import { Component } from '@angular/core';
import { HeaderComponent } from '../../layout/main-layout/header/header.component';
import { HeroComponent } from '../../layout/main-layout/hero/hero.component';
import { FooterComponent } from '../../layout/main-layout/footer/footer.component';

@Component({
  selector: 'app-new-world-home',
  standalone: true,
  imports: [HeaderComponent, HeroComponent, FooterComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class NwHomeComponent {

}
