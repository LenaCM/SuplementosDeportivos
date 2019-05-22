import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { User } from '../models/user';

@Injectable()
export class GlobalService {
    private userSource = new BehaviorSubject<User>(new User());
    user = this.userSource.asObservable();

    set me(user2: User){
        console.log(user2);
        this.userSource.next(user2);
    }
    constructor() {}
}