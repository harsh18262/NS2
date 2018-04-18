# This spec file is read by gcc when linking.  It is used to specify the
# standard libraries we need in order to link with various sanitizer libs.

*link_libasan: -lrt -lpthread -ldl -lm

*link_libtsan: -lrt -lpthread -ldl -lm

*link_libubsan: -lpthread -ldl -lm

*link_liblsan: -lpthread -ldl -lm

