import {Component, OnInit} from '@angular/core';
import {Publisher} from '../publisher';
import {PUBS} from '../publisherlist';

@Component({
  selector: 'app-publishers',
  templateUrl: './publishers.component.html',
  styleUrls: ['./publishers.component.css']
})
export class PublishersComponent implements OnInit {

  pubs: Publisher[];
  selectedPublisher: Publisher;

  constructor() {
    this.pubs = PUBS;
  }

  onSelect(publisher: Publisher): void {
    this.selectedPublisher = publisher;
  }

  ngOnInit() {
  }

}
