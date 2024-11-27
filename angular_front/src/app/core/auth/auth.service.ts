import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  // BehaviorSubject pour l'état de connexion
  private isLoggedInSubject: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(this.hasToken());
  public isLoggedIn$: Observable<boolean> = this.isLoggedInSubject.asObservable();

  // Information utilisateur
  private userInfoSubject: BehaviorSubject<any> = new BehaviorSubject<any>(this.getUserInfo());
  public userInfo$: Observable<any> = this.userInfoSubject.asObservable();

  constructor() { }

  // Vérifier si le token est présent dans le localStorage pour déterminer si l'utilisateur est connecté
  private hasToken(): boolean {
    return !!localStorage.getItem('accessToken');
  }

  // Retourner les informations de l'utilisateur stockées
  private getUserInfo(): any {
    const userInfo = localStorage.getItem('userInfo');
    return userInfo ? JSON.parse(userInfo) : null;
  }


  // Méthode pour simuler la connexion 
  fakeLogin() {
    const fakeToken = 'faceAccessToken';
    const fakeUserInfo = {
      id: 1321,
      username: 'fakeUsername',
      email: 'fake@email.com',
    };
    this.handleLoginSuccess(fakeToken, fakeUserInfo);
  }

  // Méthode pour déclencher l'événement isLoggedIn
  login() {
    
    // window.location.href = 'https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&redirect_uri=YOUR_REDIRECT_URI&response_type=token';
  }

  // Gérer la connexion réussie
  handleLoginSuccess(token: string, userInfo: any): void {
    localStorage.setItem('accessToken', token);
    localStorage.setItem('userInfo', JSON.stringify(userInfo));
    this.isLoggedInSubject.next(true);
    this.userInfoSubject.next(userInfo);
  }

  // Méthode pour se déconnecter
  logout() {
    localStorage.removeItem('accessToken');
    localStorage.removeItem('userInfo');
    this.isLoggedInSubject.next(false);
    this.userInfoSubject.next(null);
  }

  // Méthode pour obtenir l'état de connexion
  isAuthenticated(): boolean {
    return this.isLoggedInSubject.getValue();
  }

  // Méthode pour obtenir les informations de l'utilisateur
  getUserInfoSync(): any {
    return this.userInfoSubject.getValue();
  }
}
