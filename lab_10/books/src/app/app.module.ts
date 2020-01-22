import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {FormsModule} from '@angular/forms';

import { AppComponent } from './app.component';
import { AuthorsComponent } from './authors/authors.component';
import { PublishersComponent } from './publishers/publishers.component';
import { AppRoutingModule } from './app-routing.module';
import { OverviewComponent } from './overview/overview.component';
import { AuthorDetailsComponent } from './author-details/author-details.component';

@NgModule({
  declarations: [
    AppComponent,
    AuthorsComponent,
    PublishersComponent,
    OverviewComponent,
    AuthorDetailsComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
