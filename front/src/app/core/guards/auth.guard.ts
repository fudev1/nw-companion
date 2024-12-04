import { CanActivateFn, Router } from '@angular/router';
import { inject } from '@angular/core';
import { AuthService } from '../services/auth.service';


export const authGuard: CanActivateFn = (route, state) => {
  const router = inject(Router);
  const authService = inject(AuthService);


  
  if (authService.isAuthenticated) return true
  else return router.createUrlTree(['/'])
  
};

  // 1. On récupère l'objet User 
  // => currentUser$ est un observable qui retourne l'objet User
  // => utilise BehaviorSubject exposé par AuthService pour avoir un flux réactif de l'état User

  // 2. Retour de l'observable dans le guard
  // => le guard retourne un boolean ou un urlTree

  // return authService.currentUser$.pipe(
  //   map((user) => {
  //     if (user) return true
  //     else {
  //       alert('connecte toi')
  //       return router.createUrlTree(['/'])
  //     }
  //   })
  // )
