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
  todomaining = "";
  todomaindone = "";

  todoidpk = "";

  todoidstatus = "";

  // todo 상태 결정변수s
  originalstatus = true;

  // popup상태 결정변수s
  createpopup = false;
  updatepopup = true;

  // popup 에게 넘겨줄 현재 todo데이터
  transPopupStatus = false;
  transPopupTitle = "";
  transPopupContent = "";
  transPopupDuedate = "";

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
        this.todomaining = json["tdmaining"];
        this.todomaindone = json["tdmaindone"];
        console.log("tdmding", this.todomaining);
        console.log("tdmddone", this.todomaindone);
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

  // modifybutton을 클릭하였을때 ,
  // 1.popup창으로 전환,

  modifyToDo(id: string) {
    console.log("modify", id);
    this.todoidpk = id;
    this.originalstatus = false;
    this.postToDoPopup();
  }

  // status 버튼 check 시 status값 변환

  checkstatus(id: string) {
    this.todoidstatus = id;
    console.log("checkstatus", id);
    this.apiService
      .update<any>("todo/statusmodify", {
        statusid: this.todoidstatus,
      })
      .subscribe(
        (json) => {
          console.log("status success");
          location.reload();
        },
        (error) => {
          console.log("error");
        }
      );
  }

  //페이지 로딩될떄마다 db에서 todo data불러오기

  backtodo() {
    this.originalstatus = true;
  }

  //todo 에서 modify버튼 클릭시 해당 todoid에 맞는 값 back에 전송

  postToDoPopup() {
    this.apiService
      .create<any>("todo/sendtodopopup", {
        tdpopupid: this.todoidpk,
      })
      .subscribe(
        (json) => {
          console.log("popupresult", json);
          this.transPopupStatus = json["tdcurrentstatus"];
          this.transPopupTitle = json["tdcurrenttitle"];
          this.transPopupContent = json["tdcurrentcontent"];
          this.transPopupDuedate = json["tdcurrentduedate"];
          console.log("success", this.transPopupStatus);
        },
        (error) => {
          console.log("error");
        }
      );
  }
  ngOnInit(): void {
    this.getToDo();
  }
}
