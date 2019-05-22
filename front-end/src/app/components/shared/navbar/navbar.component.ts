import { Component, OnInit } from '@angular/core';
import { GlobalService } from '../../../services/services.index';
import { Router } from '@angular/router';
import { User } from '../../../models/user';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  account: User = new User();

  constructor(
    private router: Router
  ) { }

  ngOnInit() {
    if(!localStorage.getItem('token') || !localStorage.getItem('account')){
      this.router.navigate(['/login']);
    }

    this.account = JSON.parse(localStorage.getItem('account'));
    
  }

}
