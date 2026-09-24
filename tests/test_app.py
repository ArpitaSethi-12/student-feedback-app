import unittest

from app import app, feedbacks


class StudentFeedbackTestCase(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

        # Clear previous feedback before every test
        feedbacks.clear()

    # Test 1: Home page should open successfully
    def test_home_page(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Student Feedback Hub", response.data)

    # Test 2: Valid feedback should be submitted
    def test_valid_feedback_submission(self):
        response = self.client.post(
            "/",
            data={
                "name": "Arpita Sethi",
                "course": "B.Tech Data Science",
                "feedback": "The course is very informative.",
                "rating": "5"
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(feedbacks), 1)

        self.assertEqual(
            feedbacks[0]["name"],
            "Arpita Sethi"
        )

        self.assertEqual(
            feedbacks[0]["course"],
            "B.Tech Data Science"
        )

        self.assertEqual(
            feedbacks[0]["rating"],
            "5"
        )

    # Test 3: Missing name should not submit feedback
    def test_missing_name(self):
        response = self.client.post(
            "/",
            data={
                "name": "",
                "course": "B.Tech Data Science",
                "feedback": "Good course",
                "rating": "4"
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(feedbacks), 0)

    # Test 4: Missing feedback should not submit
    def test_missing_feedback(self):
        response = self.client.post(
            "/",
            data={
                "name": "Arpita",
                "course": "B.Tech Data Science",
                "feedback": "",
                "rating": "5"
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(feedbacks), 0)


if __name__ == "__main__":
    unittest.main()