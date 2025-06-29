import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private apiUrl = 'http://localhost:8000/api'; // Đổi thành URL backend của bạn

  constructor(private http: HttpClient) {}

  register(data: { username: string; password: string; email: string }): Observable<any> {
    return this.http.post(`${this.apiUrl}/register/`, data);
  }

  login(data: { username: string; password: string }): Observable<any> {
    return this.http.post(`${this.apiUrl}/login/`, data);
  }
} 