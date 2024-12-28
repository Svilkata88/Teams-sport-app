
<h2>﻿What it is about?<h2/>
 
Teams-Sport-app is a place for connecting players ( in this stage sport is only football ), allowing them to create teams, arrange matches and track the results.

<h2>Quick walk into the app:</h2>
<ul> On the app you can:
  <li>create your own team: set logo, history, additional administrators ( by default creator is the only administrator ) or just join another team</li>
  <li>manage your account: change your profile pic, change info, select team to be in ( logic for acceptance by the administrators will be applied )</li>
  <li>chat with the players in the team and public ( to be applied )</li>
  <li>create matches vs another team</li>
  <li>join tournaments</li>
  <li>rank your team with gaining wins</li>
  <li>rank yourself by playing in games and winning</li>
</ul>

<hr/>

<h2>Getting started:</h2>

<h3>1. Clone the repo e.g.</h3>

    https://github.com/Svilkata88/Teams-sport-app.git

<h3>2. Install requiremets</h3>

    pip install -r requirements.txt
    
<h3>3. Set up database and cloudinary ( optional )</h3>

<a href="https://github.com/Svilkata88/Teams-sport-app/blob/main/docs/settings_info">settings setup<a/>

<h3>4. Run migrations</h3>

    python manage.py migrate

<h3>5. Run the Django development server</h3>

    python manage.py runserver
    


Improvements plan:
1. add a lot of validators DONE
2. managing permitions for the admin section DONE
3. add chat for the players in the team
4. making the app responsive Partly DONE
5. adding rest endpoints - 2 for now
6. improve styling -DONE, can add more
7. add ratings for the players + logic for the rating
8. add turnaments - partly Done
9. deploy and test in real env Done


