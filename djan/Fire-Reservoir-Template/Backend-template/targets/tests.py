from django.test import TestCase

class TargetTestCase(TestCase):
    def test_target_creation(self):
        target = Target.objects.create(
            name="Test Target",
            attack_priority=1,
            longitude = 13.33,
            latitude = 72.89,
            enemy_organization = hamas,
            target_goal = gaza,
            was_target_destroyed = True,
            target_id = 123
        )
        self.assertEqual(target.name, "Test Target")

    def test_target_view(self):
        response = self.client.get(reverse('add_target'))
        self.assertEqual(response.status_code, 200)
