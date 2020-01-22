import { NgModule } from '@angular/core';
import {Router, RouterModule, Routes} from '@angular/router';

import { AuthorsComponent } from './authors/authors.component';
import { OverviewComponent } from './overview/overview.component';
import { AuthorDetailsComponent } from './author-details/author-details.component';

const routes: Routes = [
  { path: 'authors', component: AuthorsComponent },
  { path: 'overview', component: OverviewComponent},
  { path: 'author-details/:num', component: AuthorDetailsComponent }
];

@NgModule({
  exports: [
    RouterModule
  ],
  imports: [
    RouterModule.forRoot(routes)
  ]
})
export class AppRoutingModule { }
