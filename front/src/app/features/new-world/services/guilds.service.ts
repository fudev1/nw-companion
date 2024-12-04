import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable, map } from 'rxjs';
import { AuthService } from '../../../core/services/auth.service';
import { Guild } from '../models/guild.interface';

@Injectable({
  providedIn: 'root'
})
export class GuildsService {

  private guilds = new BehaviorSubject<Guild[]>([]);

  constructor(private auth: AuthService) { }

  getUserGuilds(): Observable<Guild[]> {
    return this.guilds.pipe(
      map(guilds => {
        const userId = this.auth.currentUser?.id;
        return guilds.filter(guild => guild.ownerId === userId);
      })
    );
  }

  createGuild(guild: Omit<Guild, 'id' | 'ownerId' | 'createdAt'>): void {
    const user = this.auth.currentUser;
    if (!user) return;

    const newGuild: Guild = {
      ...guild,
      id: crypto.randomUUID(),
      ownerId: user.id,
      createdAt: new Date()
    };

    this.guilds.next([...this.guilds.value, newGuild]);
  }

}
