from django.test import TestCase, Client
from players.models import Player
from django.urls import reverse
from players.forms import UpdatePlayerImageForm
from django.conf import settings
from django.contrib.messages import get_messages
from django.core.files.uploadedfile import SimpleUploadedFile


class TestRegisterPlayer(TestCase):
    def setUp(self):
        self.test_url = reverse('register_player')
        self.player = Player.objects.create_user(
        username='Player_1',
        password='pass1',
        )

    def test_player_register(self):
        response = self.client.get(self.test_url)

        self.assertTrue(response, self.player)
        

    def test_player_login_after_register(self):

        response = self.client.post(self.test_url, {
            'username': 'Player2',
            'password': 'pass1',
            'tel': '+359123123123',
            'confirm_password': 'pass1',
        })

        
        # checks if redirects to 'matches-dashboard' after register and loging in the player
        self.assertEqual(response.status_code, 302)

        # checks if user is loged in
        self.assertTrue('_auth_user_id' in self.client.session)
        self.assertEqual(str(self.client.session['_auth_user_id']), str(self.player.id + 1))

        follow_response = self.client.get(self.test_url)
        self.assertEqual(follow_response.status_code, 200)

       
class TestPlayerDetails(TestCase):
    def setUp(self):
        self.player = Player.objects.create_user(username='Player1', password='pass1')
        self.test_url = reverse('details-page', kwargs={'pk': self.player.pk})
        self.form = UpdatePlayerImageForm()
        self.MEDIA_URL = settings.MEDIA_URL

    # test if player is the palyer we search?
    def test_correct_player(self):
        response = self.client.get(self.test_url)

        self.assertEqual(response.status_code, 200)

    # test if the player, the form and the MEDIA_URL
    def test_correct_context_data(self):
        response = self.client.get(self.test_url)
        context = response.context

        self.assertIn('player', context)  
        self.assertIn('form', context)  
        self.assertIn('MEDIA_URL', context) 
        self.assertEqual(self.player, context['player']) 
        self.assertEqual('UpdatePlayerImageForm',  self.form.__class__.__name__)
        self.assertEqual(self.MEDIA_URL, context['MEDIA_URL']) 

    def test_correct_page_rendering(self):
        self.assertTemplateUsed('players/details-page.html')


class TestPlayerDeleteView(TestCase):
    def setUp(self):
        self.player = Player.objects.create_user(
            username="Player1",
            password="password123"
        )

        self.delete_url = reverse('delete-player', kwargs={'pk': self.player.pk})

    # test was player is deleted
    def test_player_delete(self):
        response = self.client.post(self.delete_url)

        self.assertFalse(Player.objects.filter(pk=self.player.pk).exists())

        messages = list(get_messages(response.wsgi_request))

        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), f'User {self.player.username} have been deleted!')
        self.assertRedirects(response, reverse('matches-dashboard'))

    # Attempt to delete a non-existent player
    def test_player_delete_invalid_pk(self):
        response = self.client.post(reverse('delete-player', kwargs={'pk': 9999}))
        self.assertEqual(response.status_code, 404)

    

class TestPlayerUpdateView(TestCase):

    def setUp(self):
        # Create a test player
        self.player = Player.objects.create_user(
            username="Player1",
            password="password123"
        )
        self.update_url = reverse('update-player', kwargs={'pk': self.player.pk})

    def test_correct_update_player_data(self):
        # Prepare test data for updating player information
        response = self.client.post(self.update_url, {
        'username': 'UpdatedPlayer',
        'email': 'newemail@example.com',
        'tel': '123456789',
        'first_name': 'UpdatedFirstName',
        'last_name': 'UpdatedLastName',
        })

        # Refresh the player instance from the database
        self.player.refresh_from_db()

        # Check if the player's username is updated
        self.assertEqual(self.player.username, 'UpdatedPlayer')

        # Ensure redirection after a successful update
        self.assertRedirects(response, reverse('details-page', kwargs={'pk': self.player.pk}))

    def test_update_player_invalid_form_submission(self):
        # Send POST request with empty data
        response = self.client.post(self.update_url, {}, follow=True)

        # Ensure that the form re-renders with validation errors
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'players/update-player.html')
        