import { Injectable } from "@angular/core";

@Injectable({
  providedIn: "root",
})
export class SessionService {
  constructor() {}

  // storage에 사용할 정보 저장
  setInfo(userid: string) {
    localStorage.setItem("USERNAME_ID", userid);
  }

  // storage 정보 이용
  getInfo() {
    return localStorage.getItem("USERNAME_ID");
  }

  // 로그아웃
  logOut() {
    localStorage.removeItem("USERNAME_ID");
  }
}
