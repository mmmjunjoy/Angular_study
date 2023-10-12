import { Injectable } from "@angular/core";

@Injectable({
  providedIn: "root",
})
export class SessionService {
  constructor() {}

  setInfo(username: string) {
    localStorage.setItem("USERNAME", username);
  }
}
