from rest_framework import serializers
from .models import Book

# A serializer acts as a translator between your database models and JSON.
# What it does:
# Serialization (Outbound): Automatically converts database records (Book instances) into clean JSON data.
# Deserialization & Validation (Inbound): Takes raw JSON inputs from POST requests, validates that the data format is correct (e.g., checks character lengths, makes sure required fields aren't missing), and saves them as database records.
# Without it:
# You would have to manually write all validation logic and convert model objects to dicts yourself:
# For GET: Manually write loops to construct Python dictionaries (like you did previously in views.py).
# For POST: Manually inspect request.data, check if every field exists, check field lengths, and then write code to create database rows.
class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book model instances into JSON format and validates
    incoming JSON data for creating/updating Book records.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'create_at']
