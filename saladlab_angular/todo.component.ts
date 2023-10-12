import { Component, OnInit } from "@angular/core";
import { ApiService } from "../service/api.service";
import { Router } from "@angular/router";

@Component({
  selector: "app-todo",
  templateUrl: "./todo.component.html",
  styleUrls: ["./todo.component.less"],
  providers: [ApiService],
})
export class TodoComponent implements OnInit {
  todomaindata = "";
  todoidpk = "";

  ids = document.getElementById("todoids");

  constructor(private apiService: ApiService, private router: Router) {}

  // todo 생성 팝업으로 이동
  gotodopopup() {
    this.router.navigate(["/popup"]);
  }

  // todolist db에 정보 가져오는 함수 (GET)

  getToDo() {
    this.apiService.get<any>("todo/sendtodo").subscribe(
      (json) => {
        console.log("result_todo_data:", json);
        this.todomaindata = json["tdmaindata"];
        console.log("tdmd", this.todomaindata);
      },
      (error) => {
        console.log("error");
      }
    );
  }
  // id 인자값으로 html 파일의 (tdmd[0]을 받는다)
  deleteToDo(id: string) {
    console.log(id);
    this.todoidpk = id;
    this.apiService
      .create<any>("todo/delete", {
        todopkid: this.todoidpk,
      })
      .subscribe(
        (json) => {
          console.log("gooddelete");
          this.getToDo();
        },
        (error) => {
          console.log("error");
        }
      );
  }

  //페이지 로딩될떄마다 db에서 todo data불러오기

  ngOnInit(): void {
    this.getToDo();
  }
}
