from rest_framework import serializers

from . import models

class Poi(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.djmaps
        fields = '__all__'

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.djmaps(
            gid = validated_data['gid'],
            nama = validated_data['nama'],
            alamat = validated_data['alamat'],
            kecamatan = validated_data['kecamatan'],
            keterangan = validated_data['keterangan'],
            kategori = validated_data['kategori'],
            kelurahan = validated_data['kelurahan'],
            id_kec = validated_data['id_kec'],
            id_kel = validated_data['id_kel'],
            imgpath = validated_data['imgpath'],
        )

        user.save()

        return user
