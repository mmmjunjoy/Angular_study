import { Component, OnInit } from "@angular/core";
import { ApiService } from "../service/api.service";
import { Router } from "@angular/router";

import { SessionService } from "../service/session.service";

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

  // session 사용할 변수
  useridtd = this.session.getInfo();

  // duedate 정렬 버튼 변수
  duedatebtnon = "1";

  // button result (무한변경에 사용)
  resultduedatebtn = 0;

  constructor(
    private apiService: ApiService,
    private router: Router,
    private session: SessionService
  ) {}

  // todo 생성 팝업으로 이동
  gotodopopup() {
    this.router.navigate(["/popup"]);
  }

  // todolist db에 정보 가져오는 함수 (GET)

  getToDoPlan() {
    this.apiService
      .create<any>("todo/sendtodo", {
        UserIdtd: this.useridtd,
        duedatebtn: 0,
      })
      .subscribe(
        (json) => {
          console.log("result_todo_data:", json);
          this.todomaining = json["tdmaining"];
          console.log("tdmding", this.todomaining);
        },
        (error) => {
          console.log("error");
        }
      );
  }
  getToDoDone() {
    this.apiService
      .create<any>("todo/sendtodo2", {
        UserIdtd: this.useridtd,
        duedatebtn: 0,
      })
      .subscribe(
        (json) => {
          console.log("result_todo_data:", json);
          this.todomaindone = json["tdmaindone"];
          console.log("tdmddone", this.todomaindone);
        },
        (error) => {
          console.log("error");
        }
      );
  }

  // due date -> 이른 순 또는 늦은순에 따라 정렬하기 || default -> 이른순  , 클릭시 반대값으로 정렬
  lineupDueDatePlan() {
    this.apiService
      .create<any>("todo/sendtodo", {
        UserIdtd: this.useridtd,
        duedatebtn: 1,
      })
      .subscribe(
        (json) => {
          console.log("successduedate");
          this.todomaining = json["tdmaining"];
          this.todomaindone = json["tdmaindone"];
        },
        (error) => {
          console.log("duedateerror");
        }
      );
  }
  lineupDueDateDone() {
    this.apiService
      .create<any>("todo/sendtodo2", {
        UserIdtd: this.useridtd,
        duedatebtn: 1,
      })
      .subscribe(
        (json) => {
          console.log("successduedate");
          this.todomaindone = json["tdmaindone"];
        },
        (error) => {
          console.log("duedateerror");
        }
      );
  }

  // btn의 값이 짝수인지 홀수인지에 따라 다른 정렬함수 호출
  resultplanduedate() {
    this.resultduedatebtn += 1;
    if (this.resultduedatebtn % 2 == 0) {
      this.getToDoPlan();
    } else {
      this.lineupDueDatePlan();
    }
    console.log(this.resultduedatebtn);
  }

  resultdoneduedate() {
    this.resultduedatebtn += 1;
    if (this.resultduedatebtn % 2 == 0) {
      this.getToDoDone();
    } else {
      this.lineupDueDateDone();
    }
    console.log(this.resultduedatebtn);
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
          this.getToDoPlan();
          this.getToDoDone();
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

  // Log Out -> session  정보값 remove , 이동하기 -> 홈으로

  logout() {
    this.session.logOut();
    this.router.navigate([""]);
  }

  ngOnInit(): void {
    this.getToDoPlan();
    this.getToDoDone();
  }
}
