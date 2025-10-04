# add_sample_users.py
from django.contrib.auth.models import User
from dating.models import Profile, Interest
import random

def create_sample_users():
    sample_users = [
        {
            'username': 'alex_adventurer',
            'first_name': 'Alex',
            'last_name': 'Morgan',
            'bio': 'Professional photographer and world traveler. Always seeking the next adventure and meaningful connections.',
            'location': 'Colorado',
            'interests': ['Travel', 'Photography', 'Hiking']
        },
        {
            'username': 'sarah_creative', 
            'first_name': 'Sarah',
            'last_name': 'Chen',
            'bio': 'UX designer and art gallery owner. Love creative minds and deep conversations over coffee.',
            'location': 'San Francisco',
            'interests': ['Art', 'Design', 'Coffee']
        },
        {
            'username': 'mike_innovator',
            'first_name': 'Mike',
            'last_name': 'Rodriguez', 
            'bio': 'Tech entrepreneur and musician. Building the future by day, creating music by night.',
            'location': 'Austin',
            'interests': ['Technology', 'Music', 'Innovation']
        }
    ]
    
    for user_data in sample_users:
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            defaults={
                'first_name': user_data['first_name'],
                'last_name': user_data['last_name'],
                'email': f'{user_data[\"username\"]}@example.com'
            }
        )
        
        if created:
            user.set_password('password123')
            user.save()
            print(f'✅ Created user: {user.username}')
        
        if not hasattr(user, 'profile'):
            profile = Profile.objects.create(
                user=user,
                bio=user_data['bio'],
                location=user_data['location']
            )
            # Add interests
            for interest_name in user_data['interests']:
                interest, _ = Interest.objects.get_or_create(name=interest_name)
                profile.interests.add(interest)
            
            print(f'✅ Created profile for: {user.username}')

if __name__ == '__main__':
    create_sample_users()
    print('🎉 Sample users added successfully!')
