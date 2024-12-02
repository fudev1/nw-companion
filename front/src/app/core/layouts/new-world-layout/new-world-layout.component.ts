import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NewWorldNavComponent } from "../../navigation/new-world-nav/new-world-nav.component";

@Component({
  selector: 'app-new-world-layout',
  standalone: true,
  imports: [
    RouterOutlet,
    NewWorldNavComponent, 
    NewWorldNavComponent
],
  templateUrl: './new-world-layout.component.html',
  styleUrl: './new-world-layout.component.scss'
})
export class NewWorldLayoutComponent {

}
