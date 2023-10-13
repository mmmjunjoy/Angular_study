import { Component, OnInit, Input, Output, EventEmitter } from "@angular/core";
import { ApiService } from "../service/api.service";
import { Router } from "@angular/router";
import { TodoComponent } from "../todo/todo.component";

@Component({
  selector: "app-popup",
  templateUrl: "./popup.component.html",
  styleUrls: ["./popup.component.less"],
})
export class PopupComponent implements OnInit {
  @Input() todoid = "";
  // popup 역할 - 1.create , 2. update  | default 는 createmode
  @Input() createmode = true;
  @Input() updatemode = false;

  // /todo 기본으로 돌아가기 위한  , 자식에서 부모로 상태값 넘기기 위한 변수
  @Output() originalstate = new EventEmitter<boolean>();

  todostatus = "";
  todotitle = "";
  todocontent = "";
  tododuedate = "";

  constructor(private ApiServices: ApiService, private router: Router) {}

  // tododata check  함수 -> 확인  ok
  checktododata() {
    console.log("status:", this.todostatus);
    console.log("title:", this.todotitle);
    console.log("content:", this.todocontent);
    console.log("duedata:", this.tododuedate);
  }

  // popup창 취소 버튼 구현

  popupcancle() {
    this.router.navigate(["/todo"]);
  }

  backtoorigin(value: boolean) {
    this.originalstate.emit(value);
  }

  // todo db에 data 보내기

  PostToDoData() {
    this.ApiServices.create<any>("todo/create", {
      tdstatus: this.todostatus,
      tdtitle: this.todotitle,
      tdcontent: this.todocontent,
      tdduedate: this.tododuedate,
    }).subscribe(
      (json) => {
        console.log("good");
        this.router.navigate(["/todo"]);
      },
      (error) => {
        console.log("error");
        alert("필수 항목을 입력해주세요.");
      }
    );
  }

  ngOnInit(): void {}
}
