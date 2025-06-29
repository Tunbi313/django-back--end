import { Component } from '@angular/core';
import { HeaderComponent } from '../../component/header/header.component';
import { FormsModule } from '@angular/forms';
import { AuthService } from '../../api/auth.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  imports: [HeaderComponent, FormsModule, CommonModule]
})
export class LoginComponent {
  username = '';
  password = '';
  message = '';
  error = '';

  constructor(private authService: AuthService) {}

  onSubmit() {
    this.message = '';
    this.error = '';
    this.authService.login({ username: this.username, password: this.password })
      .subscribe({
        next: (res) => { this.message = res.message; },
        error: (err) => { this.error = err.error?.error || 'Đăng nhập thất bại'; }
      });
  }
} 