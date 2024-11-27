import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { LoginButtonComponent } from "../login-button/login-button.component";

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [RouterModule, LoginButtonComponent],
  templateUrl: './header.component.html',
  styleUrl: './header.component.scss'
})
export class HeaderComponent {

}
