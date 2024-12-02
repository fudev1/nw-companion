import { CanActivateFn, Router } from '@angular/router';
import { Inject } from '@angular/core';
import { AuthService } from '../services/auth.service';

export const authGuard: CanActivateFn = (route, state) => {
  const router = Inject(Router);
  const authService = Inject(AuthService)

  if (authService.isAuthenticated) return true
  else {
    alert('connecte toi')
    return router.createUrlTree(['/'])
  }
};
