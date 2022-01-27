import { Component } from '@angular/core';
import {ApiService} from "./api.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  providers: [ApiService]
})
export class AppComponent {
  chapters = [{text: 'test'}];
  constructor(private api:ApiService) {
    this.getChapters();
  }
  getChapters = () => {
    this.api.getAllChapters().subscribe(
      data => {
        this.chapters = data;

      },
      error => {
        console.log(error);
    }
    )
  }
}
