
PROTOBUF_SRC=./protobuf
GOLANG_DST=./
PYTHON_DST=./python/messages

protofiles: ${PROTOBUF_SRC}
	protoc -I=${PROTOBUF_SRC} --go_out=${GOLANG_DST} \
		--python_out=${PYTHON_DST} \
		${PROTOBUF_SRC}/*.proto

