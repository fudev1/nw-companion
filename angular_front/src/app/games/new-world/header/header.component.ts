import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { LoginButtonComponent } from '../../../core/layout/login-button/login-button.component';
@Component({
  selector: 'app-new-world-header',
  standalone: true,
  imports: [RouterModule, LoginButtonComponent],
  templateUrl: './header.component.html',
  styleUrl: './header.component.scss'
})
export class NewWorldHeaderComponent {

}
