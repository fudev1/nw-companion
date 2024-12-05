import { Component, Input } from '@angular/core';
import { Build } from '../../../models/build.interface';

@Component({
  selector: 'app-character-build',
  standalone: true,
  imports: [],
  templateUrl: './character-build.component.html',
  styleUrl: './character-build.component.scss'
})
export class CharacterBuildComponent {
  @Input({ required: true }) characterId!: string;
}
